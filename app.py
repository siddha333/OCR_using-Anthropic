import fitz  # PyMuPDF
import pytesseract
from PIL import Image
import openai
import os

def extract_text_from_pdf(pdf_path):
    text = ""
    # Open the PDF file
    with fitz.open(pdf_path) as doc:
        # Iterate through each page
        for page_num in range(len(doc)):
            page = doc.load_page(page_num)
            text += page.get_text()
    return text

def extract_text_from_image(image_path):
    # Use Tesseract OCR to extract text from the image
    text = pytesseract.image_to_string(Image.open(image_path))
    return text

# Example usage
pdf_text = extract_text_from_pdf("Tata AIG Motor Policy Schedule_3184_6202287894-00.pdf")
#image_text = extract_text_from_image("example_image.png")

#print("Text from PDF:")
#print(pdf_text)





# # Set your OpenAI API key
# api_key ='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'

# client = openai.OpenAI(api_key=api_key)

# def ask_llm(context, question, model="text-davinci", max_tokens=100):
#     prompt = f"Context: {context}\nQuestion: {question}\nAnswer:"
#     chat_completion = client.chat.completions.create(
#         messages=[
#             {"role": "user", "content": prompt}
#         ],
#         model=model,
#         max_tokens=max_tokens
#     )
#     return chat_completion.choices[0].message['content'].strip()
# # Example usage
# pdf_text = "Text extracted from your PDF"
# question = "What is the total amount due?"

# # Pass the extracted text and question to the LLM and get response
# response_pdf = ask_llm(pdf_text, question)

# print("Response from LLM (PDF):")
# print(response_pdf)


from anthropic import Anthropic

client = Anthropic(
    api_key="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",
)

def ask_llm(question, context, model="claude-3-opus-20240229", max_tokens=1024):
    prompt = f"Context: {context}\nQuestion: {question}\nAnswer:"
    message = client.messages.create(
        max_tokens=max_tokens,
        messages=[
            {"role": "user", "content": prompt}
        ],
        model=model
    )
    return message.content

pdf_path = "Tata AIG Motor Policy Schedule_3184_6202287894-00.pdf"
pdf_text = extract_text_from_pdf(pdf_path)
question = "What is the address of the person?"

# Pass the extracted text and question to the LLM and get response
response_pdf = ask_llm(question, pdf_text)

print("Response from Anthropic (PDF):")
print(response_pdf)


