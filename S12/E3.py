from abc import ABC, abstractmethod

class CommunicationModule(ABC):
    @abstractmethod
    def log_in(self, credentials):
        pass

    @abstractmethod
    def set_id(self, network_id):
        pass

    @abstractmethod
    def get_id(self):
        pass


class TemperatureSensor:
    def temp_connect(self):
        self.connected_temp = True
        print(f"Sensor de temperatura {self.device_id} conectado.")

    def temp_disconnect(self):
        self.connected_temp = False
        print(f"Sensor de temperatura {self.device_id} desconectado.")

    def read_temperature(self):
        if getattr(self, "connected_temp", False):
            temp = 22.5
            print(f"Sensor de temperatura {self.device_id} leyendo: {temp}°C")
            return temp
        else:
            print(f"Sensor de temperatura {self.device_id} no está conectado. No se puede leer.")
            return None


class SmartLight:
    def light_on(self):
        self.connected_light = True
        self.brightness = getattr(self, "brightness", 100)
        print(f"Bombillo {self.device_id} encendido. Brillo: {self.brightness}%")

    def light_off(self):
        self.connected_light = False
        print(f"Bombillo {self.device_id} apagado.")

    def set_brightness(self, level: int):
        self.brightness = max(0, min(100, int(level)))
        print(f"Bombillo {self.device_id} brillo ajustado a {self.brightness}%")
        if getattr(self, "connected_light", False):
            print(f"Bombillo {self.device_id} aplica brillo {self.brightness}% ahora.")


class SecurityCamera:
    def camera_start(self):
        self.connected_camera = True
        self.recording = True
        print(f"Cámara {self.device_id} iniciada. Grabando: {self.recording}")

    def camera_stop(self):
        self.recording = False
        self.connected_camera = False
        print(f"Cámara {self.device_id} detenida.")

    def take_snapshot(self):
        if getattr(self, "connected_camera", False):
            print(f"Cámara {self.device_id} tomando snapshot.")
        else:
            print(f"Cámara {self.device_id} no está activa. No se puede tomar snapshot.")


class IoTDevice(TemperatureSensor, SmartLight, SecurityCamera, CommunicationModule):
    def __init__(self, device_id):
        self.device_id = device_id
        self.connected_temp = False
        self.connected_light = False
        self.connected_camera = False
        self.brightness = 100
        self.recording = False
        self._network_id = None
        self._logged_in = False

    # Implementación de CommunicationModule como métodos abstractos.
    def log_in(self, credentials):
        self._logged_in = True
        print(f"Dispositivo {self.device_id} logueado con credenciales: {credentials}")

    def set_id(self, network_id):
        self._network_id = network_id
        print(f"Dispositivo {self.device_id} asociado a network id: {self._network_id}")

    def get_id(self):
        print(f"Dispositivo {self.device_id} network id: {self._network_id}")
        return self._network_id