import Utils
import json

class PredictionHandler(object):
    def __init__(self, gpr):
        self.gpr = gpr
    
    def handle_request(request):
        check_request(request)
        #if(request["type"] == "graph"):
        return handle_graph_request(request)
    
    def handle_graph_request(req):
        area = req["area"]
        
        # Check if we should explicity (re)generate predictions
        generate = "regenerate" in req and req["regenerate"]     
        
        # Check for (lack of) predictions json file
        pred_path = pred_save_path + dataset + "/" + model + "/" + area + ".json"      
        timestamp_path = pred_save_path + dataset + "/" + model + "/timestamp_" + area + ".json"
        if(not os.path.isfile(pred_path)):
            # Check if already being generated
            if(os.path.isfile(timestamp_path)):
                # Check generation hasn't timed out (<2 hours since)
                with open(timestamp_path) as timestamp_file:                            
                    timestamp_obj = json.load(timestamp_file)
                    if(Utils.timestamp() - timestamp_obj["timestamp"] < 7200 and not generate):
                        return {                                                                        # Respond with status message
                            "status": 301,
                            "message": "Gaussian process generation & prediction is already in progress for: " + area
                        }
            else:
                Utils.create_folder(pred_save_path)                # If no files found, create appropriate folders
                Utils.create_folder(pred_save_path + dataset)
                Utils.create_folder(pred_save_path + dataset + "/" + model)
            generate = True                                                     # If not present, request predictions generation  

        if(generate):
            with open(timestamp_path, 'w') as outfile:           
                json.dump({ "timestamp": Utils.timestamp() }, outfile)          # Timestamp our new predictions generation
            self.gpr.generate({             
                "dataset": dataset,
                "model": model,
                "area": area
            }, await_response=False)
            return {                                                                        # Respond with status message
                "status": 300,
                "message": "Gaussian process generation & prediction has now started for area: " + area
            }

        with open(pred_path) as pred_file:                                                    # Otherwise respond with predictions
            return {
                "status": 200,
                "results": json.load(pred_file)
            }
    
    def status_response(num, message):
        return { "status":num, "message": message }
            
    def check_request(req):
        if("datatset" not in req):
            print("err")
            
        if("model" not in req):
            print("err")    
        
        if("area" not in req):                                                              
        # Get area name from request
            return status_response(402, "No area given in prediction request")    
            
        dataset = str(req["dataset"])
        
        model = str(req["model"])

        if(dataset != "landreg"):                                                      
        # Check dataset exists
            return status_response(400, "Unknown dataset '" + dataset + "'.")
        
        # Check model exists
        with open('model_parameters.json') as model_params_file:                            
            all_model_params = json.load(model_params_file)
        
        models_for_dataset = all_model_params[dataset]
        if(not model in models_for_dataset):
            return status_response(401, "Unknown model '" + model + "' for dataset '" + dataset + "'.")

        
