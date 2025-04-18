import gradio as gr
from huggingface_hub import InferenceClient


client = InferenceClient("black-forest-labs/FLUX.1-dev", token="use urs token")


def generate_image(prompt):
    image = client.text_to_image(prompt)
    return image


# Adding a title to the Gradio interface
iface = gr.Interface(fn=generate_image, 
                     inputs=gr.Textbox(label="Enter Text Prompt"), 
                     outputs=gr.Image(type="pil", label="Generated Image"),
                     title="TEXT-TO_IMAGE GENERATION USING FLUX.1-dev",
                     flagging_options=["average","good","bad"])


iface.launch(share=True)
