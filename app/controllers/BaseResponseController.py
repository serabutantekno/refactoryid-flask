class BASE_RESPONSE():

    def base_response(self, message=None, data=[], status_code=200):
        if type(data) is not list:
            result = []
            result.append(data)
        else:
            result = data
        
        return {
            "message": message,
            "data": result
        }, status_code
    
    
    def error(self):
        return self.base_response(message="something error", status_code=500)
    

    def data_not_found(self):
        return self.base_response(message="data not found", status_code=404)
