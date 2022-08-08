from fastapi import FastAPI
from transformers import BertTokenizer, TFBertForSequenceClassification, BertConfig, TextClassificationPipeline

tokenizer = BertTokenizer.from_pretrained('dbmdz/bert-base-turkish-128k-uncased', do_lower_case=True)

config = BertConfig.from_json_file("static/model_files/bigscience_t0_model/config.json")
model_path = "static/model_files/bigscience_t0_model"
tokenizer_path = "static/model_files/bigscience_t0_tokenizer"

model = TFBertForSequenceClassification.from_pretrained(model_path, from_pt=True)

app = FastAPI()


@app.get("/{text}")
async def get_label_score(text: str):
    pipe = TextClassificationPipeline(model=model, tokenizer=tokenizer)
    return {"success": True,
            "payload": pipe(text)
            }
