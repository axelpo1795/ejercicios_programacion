from abc import ABC, abstractmethod

class IoTDevice(ABC):
    
    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def disconnect(self):
        pass

    @abstractmethod
    def send_data(self, data):
        pass

class TemperatureSensor(IoTDevice):
    def __init__(self, device_id):
        self.device_id = device_id
        self.connected = False

    def connect(self):
        self.connected = True
        print(f"Sensor de temperatura {self.device_id} conectado.")

    def disconnect(self):
        self.connected = False
        print(f"Sensor de temperatura {self.device_id} desconectado.")
    def send_data(self, data):
        if self.connected:
            print(f"Sensor de temperatura {self.device_id} enviando datos: {data}")
        else:
            print(f"Sensor de temperatura {self.device_id} no está conectado. No se pueden enviar datos.")

class SmartLight(IoTDevice):
    def __init__(self, device_id):
        self.device_id = device_id
        self.connected = False

    def connect(self):
        self.connected = True
        print(f"Bombillo inteligente {self.device_id} conectada.")

    def disconnect(self):
        self.connected = False
        print(f"Bombillo inteligente {self.device_id} desconectada.")
    def send_data(self, data):
        if self.connected:
            print(f"Bombillo inteligente {self.device_id} enviando datos: {data}")
        else:
            print(f"Bombillo inteligente {self.device_id} no está conectada. No se pueden enviar datos.")

class SecurityCamera(IoTDevice):
    def __init__(self, device_id):
        self.device_id = device_id
        self.connected = False

    def connect(self):
        self.connected = True
        print(f"Cámara de seguridad {self.device_id} conectada.")

    def disconnect(self):
        self.connected = False
        print(f"Cámara de seguridad {self.device_id} desconectada.")
    def send_data(self, data):
        if self.connected:
            print(f"Cámara de seguridad {self.device_id} enviando datos: {data}")
        else:
            print(f"Cámara de seguridad {self.device_id} no está conectada. No se pueden enviar datos.")