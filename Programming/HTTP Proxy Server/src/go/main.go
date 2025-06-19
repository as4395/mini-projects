package main

import (
	"bufio"
	"fmt"
	"io"
	"log"
	"net"
	"strings"
)

// Keywords considered suspicious in HTTP traffic
var suspiciousKeywords = []string{"password", "credit card", "login", "attack", "malware"}

// containsSuspiciousContent checks if any suspicious keyword is found in data
func containsSuspiciousContent(data string) bool {
	lowerData := strings.ToLower(data)
	for _, keyword := range suspiciousKeywords {
		if strings.Contains(lowerData, keyword) {
			return true
		}
	}
	return false
}

// handleConnection manages incoming client requests and forwards them to the destination server
func handleConnection(clientConn net.Conn) {
	defer clientConn.Close()

	reader := bufio.NewReader(clientConn)
	requestLine, err := reader.ReadString('\n')
	if err != nil {
		log.Println("Error reading request line:", err)
		return
	}
	fmt.Printf("Request: %s", requestLine)

	parts := strings.Fields(requestLine)
	if len(parts) < 3 {
		log.Println("Malformed request line")
		return
	}
	method, path, protocol := parts[0], parts[1], parts[2]

	headers := make(map[string]string)
	for {
		line, err := reader.ReadString('\n')
		if err != nil {
			log.Println("Error reading headers:", err)
			return
		}
		line = strings.TrimSpace(line)
		if line == "" {
			break // End of headers
		}
		headerParts := strings.SplitN(line, ":", 2)
		if len(headerParts) != 2 {
			continue
		}
		headers[strings.TrimSpace(headerParts[0])] = strings.TrimSpace(headerParts[1])
	}

	hostPort := headers["Host"]
	if hostPort == "" {
		log.Println("Host header missing; cannot forward request.")
		return
	}
	if !strings.Contains(hostPort, ":") {
		hostPort += ":80"
	}

	serverConn, err := net.Dial("tcp", hostPort)
	if err != nil {
		log.Println("Error connecting to server:", err)
		return
	}
	defer serverConn.Close()

	// Send the client's request line and headers to the server
	fmt.Fprintf(serverConn, "%s %s %s\r\n", method, path, protocol)
	for k, v := range headers {
		fmt.Fprintf(serverConn, "%s: %s\r\n", k, v)
	}
	fmt.Fprint(serverConn, "\r\n")

	// Relay the server's response back to the client, checking for suspicious content
	buf := make([]byte, 4096)
	for {
		n, err := serverConn.Read(buf)
		if n > 0 {
			data := string(buf[:n])
			if containsSuspiciousContent(data) {
				log.Println("Alert: Suspicious keyword detected in response")
			}
			_, writeErr := clientConn.Write(buf[:n])
			if writeErr != nil {
				log.Println("Error writing to client:", writeErr)
				return
			}
		}
		if err != nil {
			if err != io.EOF {
				log.Println("Error reading from server:", err)
			}
			break
		}
	}
}

func main() {
	listenAddr := "localhost:8888"
	ln, err := net.Listen("tcp", listenAddr)
	if err != nil {
		log.Fatalf("Failed to listen on %s: %v", listenAddr, err)
	}
	log.Printf("HTTP proxy server started on %s", listenAddr)

	for {
		conn, err := ln.Accept()
		if err != nil {
			log.Println("Error accepting connection:", err)
			continue
		}
		go handleConnection(conn)
	}
}
