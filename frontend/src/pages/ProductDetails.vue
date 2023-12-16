<template>
  <div>
    <div class="typography">Product Details</div>
    <div class="bg"></div>
  </div>
  <div class="product-details">
    <img :src="product.image" alt="Product Image" width="300" />
    <h2>{{ product.name }}</h2>
    <h4>{{ product.description }}</h4>
    <div class="flex">
      <h4 class="productPrice">Rs. {{ product.price }}</h4>
      <div class="quantity">
        <button class="addBtn" @click="decreaseQuantity">-</button>
        <span class="productQty">{{ quantity }}</span>
        <button class="addBtn" @click="increaseQuantity">+</button>
      </div>
      <button class="cartbtn" @click="addToCart">Add to Cart</button>
    </div>
  </div>
</template>

<script>
import { API_URL } from "../constants";

export default {
  data() {
    return {
      product: {
        name: "",
        image: "",
        description: "",
        price: 0,
      },
      quantity: 0,
    };
  },
  methods: {
    increaseQuantity() {
      this.quantity++;
    },
    decreaseQuantity() {
      if (this.quantity > 1) {
        this.quantity--;
      }
    },
    async addToCart() {
      try {
        await fetch(API_URL + "/cart", {
          method: "POST",
          body: JSON.stringify({
            product_id: this.$route.params.id,
            quantity: this.quantity,
          }),
          headers: {
            "Content-Type": "application/json",
            Authorization: "Bearer " + localStorage.getItem("token"),
          },
        });
      } catch (e) {
        console.error(e);
      }
    },
    getProduct() {
      fetch(API_URL + "/product/" + this.$route.params.id)
        .then(async (response) => await response.json())
        .then((data) => (this.product = data));
    },
  },
  mounted() {
    this.getProduct();
  },
};
</script>

<style scoped>
.product-details {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  margin-top: 2rem;
  margin-bottom: 2rem;
}

.quantity {
  display: flex;
  align-items: center;
}

.productData {
  padding-top: 1rem;
  font-size: 1.3rem;
  font-style: normal;
  font-weight: 500;
  line-height: normal;
}
.productPrice {
  padding-top: 0.5rem;
  color: #23aa49;
  font-size: 36px;
  font-style: normal;
  font-weight: 700;
  line-height: normal;
}
.productQty {
  padding-top: 0.5rem;
  padding-left: 0.8rem;

  color: #23aa49;
  font-size: 2rem;
  font-style: normal;
  font-weight: 700;
  line-height: normal;
}
.addBtn {
  border-radius: 20%;
  padding: 5px 15px;
  background: #23aa49;
  color: white;
  font-size: 2rem;
}
.cartbtn {
  position: absolute;
  bottom: 10%;
  right: 10%;
  background: #23aa49;
  color: white;
  display: flex;
  justify-content: center;
  align-items: center;
  font-size: 2rem;
  border: none;
  cursor: pointer;
  border-radius: 25px;
  padding: 5px;
  width: 200px;
  height: 50px;
}
</style>
