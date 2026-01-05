from fastapi import FastAPI

app = FastAPI(title="Product Service")

products = []

@app.get("/")
def health():
    return {"service": "product", "status": "running"}

@app.post("/products")
def add_product(name: str, price: float):
    products.append({"name": name, "price": price})
    return {"message": "Product added"}

@app.get("/products")
def get_products():
    return products
