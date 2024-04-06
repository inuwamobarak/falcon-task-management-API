# from .foundation import LMMistral
# from resources import TaskCollectionResource

# import torch


# class AiModel:

#     def __init__(self):
#         pass


#     def _generate_bot_response(self, prompt, task_id, title, description):
        
#         self.mistral_instance = LMMistral()

#         self.task_id = TaskCollectionResource.id
#         self.title = TaskCollectionResource.title
#         self.description = TaskCollectionResource.description

#         try:
#             prompt = f"""<s>[INST]Based on the following task, can you give the user tips and recommendations to finish them well?. 
#             Task ID: {task_id}, Title: {title}, and Description: {description}            
#             [/INST]"""

#             result = self.mistral_instance.pipe(prompt)

#             return result[0]['generated_text']
#         except Exception as e:
#             print(f"Error in inference: {e}")

#             return None

#     def fitness_ai(self, prompt):
#         return self._generate_bot_response(prompt, 'FitMateBot')