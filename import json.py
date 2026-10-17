import json
from datetime import datetime
from typing import List, Dict

class SatelliteTelementry:
    def __init__(self, satellite_id: str):
        self.satellite_id = satellite_id
        self.data_points: List[Dict] = []
    
    def add_telemetry(self, timestamp: str, altitude: float, temp: float, 
                      power: float, signal_strength: float):
        """Add telemetry data point"""
        self.data_points.append({
            "timestamp": timestamp,
            "altitude_km": altitude,
            "temp_celsius": temp,
            "power_percent": power,
            "signal_strength_db": signal_strength
        })
    
    def get_average_values(self) -> Dict:
        """Calculate average telemetry values"""
        if not self.data_points:
            return {}
        
        return {
            "avg_altitude": sum(p["altitude_km"] for p in self.data_points) / len(self.data_points),
            "avg_temp": sum(p["temp_celsius"] for p in self.data_points) / len(self.data_points),
            "avg_power": sum(p["power_percent"] for p in self.data_points) / len(self.data_points),
            "avg_signal": sum(p["signal_strength_db"] for p in self.data_points) / len(self.data_points)
        }
    
    def check_anomalies(self, temp_threshold: float = 80) -> List[Dict]:
        """Detect anomalies in telemetry"""
        anomalies = [p for p in self.data_points if p["temp_celsius"] > temp_threshold]
        return anomalies

# Example usage
sat = SatelliteTelementry("SAT-001")
sat.add_telemetry("2024-01-15 10:00:00", 400, 25, 85, -120)
sat.add_telemetry("2024-01-15 10:05:00", 401, 28, 83, -118)
print(sat.get_average_values())