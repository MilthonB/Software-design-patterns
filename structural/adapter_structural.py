

"""
Ejemplos de uso: El patrón Adapter es muy común en el código Python. Se utiliza muy a menudo en sistemas basados en algún código heredado. 
En estos casos, los adaptadores crean código heredado con clases modernas.

Identificación: Adapter es reconocible por un constructor que toma una instancia de distinto tipo de clase abstracta/interfaz. Cuando el adaptador 
recibe una llamada a uno de sus métodos, convierte los parámetros al formato adecuado y después dirige la llamada a uno o varios métodos del objeto envuelto.

https://refactoring.guru/es/design-patterns/adapter/python/example


"""
class DataEntity:
    def __init__(self, data: str, status: int, code: str, message: str, timestamp: str):
        self.data = data
        self.status = status
        self.code = code
        self.message = message
        self.timestamp = timestamp


class ProviderAPiDummy:
    def specific_request(self) -> dict:
        return {
            "data": "response from Provider A API",
            "status": 200,
            "code": "OK",
            "message": "Success",
            "timestamp": "2024-10-10T10:00:00Z"
        }


class ProviderAPIAdapter:
    def __init__(self, provider_api: ProviderAPiDummy) -> None:
        self.provider_api = provider_api

    def request(self) -> DataEntity:
        response =  self.provider_api.specific_request()
        return DataEntity(
            data=response["data"],
            status=response["status"],
            code=response["code"],
            message=response["message"],
            timestamp=response["timestamp"]
        )


if __name__ == "__main__":
    provider_api = ProviderAPiDummy()
    adapter = ProviderAPIAdapter(provider_api=provider_api)
    data_entity = adapter.request()
    print(f"Data: {data_entity.data}")
    print(f"Status: {data_entity.status}")
    print(f"Code: {data_entity.code}")
    print(f"Message: {data_entity.message}")
    print(f"Timestamp: {data_entity.timestamp}")

