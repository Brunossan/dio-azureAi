import streamlit as st
from services.bolb_service import upload_file_to_blob
from services.credit_card_service import analyze_credit_card

def configure_interface():
  st.title("up arq DIO - docs")
  uploaded_file = st.file_uploader("escolha um arquivo", type = ["png", "jpg"])

  if uploaded_file is not None:
    fileName = uploaded_file.name
    
    # Enviar pro BLOB
    blob_url = upload_file_to_blob(uploaded_file, fileName)
    if blob_url:
      st.write(f"Arquivo {fileName} enviado com sucesso")
      credit_card_info = ""
      show_image_and_validation(blob_url, credit_card_info)
    else:
      st.write(f"Error")

def show_image_and_validation(blob_url, credit_card_info):
  st.image(blob_url, caption="Img", use_column_width=True)
  st.write("infos encontradas")
  if credit_card_info and credit_card_info["card_name"]:
    st.image(credit_card_info)
    st.write(f"Titular: {credit_card_info["card_name"]}")


if __name__ == "__main__":
  configure_interface()
