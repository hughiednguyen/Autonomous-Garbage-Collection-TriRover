server_address = "192.168.43.36"
port = 1883
username = "server_observer"
password = "team15"
filename = "statistics.json"

topics = [
    "statistics",
    "trirover_status",
    "arm_status",
    "sensors_status",
    "track_rover_status"
]

subscribers = {
    "trirover_status": ["arm"],
    "arm_status": ["track_rover", "sensors"],
    "sensors_status": ["trirover"],
    "track_rover_status": ["arm"]
}

board_id = ["trirover", "track_rover", "arm", "sensors"]
