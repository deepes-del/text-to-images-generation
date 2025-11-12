import gradio as gr  # user can change the interface framwork accordingly
from huggingface_hub import InferenceClient  #imported the brain on the model from the hugging face


client = InferenceClient("black-forest-labs/FLUX.1-dev", token="use your own  token")
#you can also use the local llm for the image geneartion , with the minimun requriments of the system.


def generate_image(prompt):
    image = client.text_to_image(prompt)
    return image


#  u can chnage the interface  as user need and framwork
iface = gr.Interface(fn=generate_image, 
                     inputs=gr.Textbox(label="Enter Text Prompt"), 
                     outputs=gr.Image(type="pil", label="Generated Image"),
                     title="TEXT-TO_IMAGE GENERATION USING FLUX.1-dev",
                     flagging_options=["average","good","bad"])


iface.launch(share=True)#for getting the public acces links use the share parameter to true always 






