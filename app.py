import gradio as gr
from modelscope.pipelines import pipeline

# Initialize the crowd counting pipeline
model = pipeline('crowd-counting')

def count_crowd(image):
    # Perform crowd counting
    result = model(image)
    crowd_count = int(result['scores'])
    return f"<div style='font-size: 40px; color: #333; text-align: center;'>Total Crowd Count: {crowd_count}</div>"

def clear_input():
    return gr.update(value=None)

# Create the Gradio interface
with gr.Blocks() as demo:
    gr.Markdown("## Crowd Counting App")
    
    with gr.Row():
        with gr.Column():
            image_input = gr.Image(type="pil")
            submit_button = gr.Button("Count Crowd")
            reset_button = gr.Button("Upload Another Image")
        with gr.Column():
            output_html = gr.HTML()

    submit_button.click(fn=count_crowd, inputs=image_input, outputs=output_html)
    reset_button.click(fn=clear_input, inputs=None, outputs=image_input)

# Launch the Gradio app
demo.launch()
