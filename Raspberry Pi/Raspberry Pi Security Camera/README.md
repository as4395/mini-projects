# Raspberry Pi Security Camera

This project sets up a motion-detecting security camera using your Raspberry Pi and a compatible USB or Pi Camera module. It uses `motion` software to stream and record video when motion is detected.

## Features

- Real-time motion detection
- Video recording and snapshot capture
- Web streaming interface (MJPEG)
- Lightweight and low resource usage

## Installation

```bash
sudo apt update
sudo apt install motion -y
```

## Configuration Steps

**1.** Enable the camera module (if using Pi Camera):
```bash
sudo raspi-config
```
Navigate to **Interface Options > Camera > Enable**

**2.** Clone the project:
```bash
git clone https://github.com/as4395/Mini-Projects.git
cd Mini-Projects/RaspberryPi/security-camera
```

**3.** Make config changes:
```bash
sudo cp config/motion.conf /etc/motion/motion.conf
```

**4.** Start motion daemon:
```bash
sudo systemctl enable motion
sudo systemctl start motion
```

**5.** Access stream in browser:
```
http://<Raspberry_Pi_IP>:8081
```

## Output

Captured images/videos will be stored in `/var/lib/motion/`.

## Notes

- You may need to edit `/etc/motion/motion.conf` to change resolution, frame rate, and detection sensitivity.
- **`/src` folder is not used** as `motion` handles the logic. Only config file is used.
