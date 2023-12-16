<template>
  <div class="productcard">
    <div class="padding">
      <RouterLink class="linker" :to="`/productdetails/${id}`">
      <img :src="image" alt="Image" top />
      
      <div class="productData">
        
          Name: {{ name }}
        
      </div>
    </RouterLink>
      <div class="flex">
        <div class="productPrice">Rs.{{ price }}</div>
        <button class="addBtn" @click="decrement">-</button>
        <div class="productQty">{{ quantity }}</div>
        <button class="addBtn" @click="increment">+</button>
      </div>
    </div>
    <button class="cartbtn" @click="addToCart">Add To Cart</button>
  </div>
</template>

<script>
import { API_URL } from "../constants";

export default {
  data: () => ({
    quantity: 1,
  }),
  props: {
    id: Number,
    name: String,
    price: Number,
    availableQuantity: Number,
    categoryId: Number,
    image: String,
  },
  methods: {
    increment() {
      this.quantity++;
    },
    decrement() {
      if (this.quantity > 1) {
        this.quantity--;
      }
    },
    async addToCart() {
      try {
        await fetch(API_URL + "/cart", {
          method: "POST",
          body: JSON.stringify({
            product_id: this.id,
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
  },
};
</script>

<style>
.linker {
  text-decoration: none;
  color: white;
  cursor: pointer;
}
.linker:hover {
  color: #23aa49;
}
.padding {
  margin: 10%;
}
.productcard {
  width: 11rem;
  height: 17rem;
  border-radius: 16px;
  background: #1a3848;
  overflow: hidden;
}
.productcard img {
  width: 100%;
  border-radius: 16px;
  height: 7rem;
}
.productData {
  padding-top: 1rem;
  font-size: 1.3rem;
  font-style: normal;
  font-weight: 500;
  line-height: normal;
}
.productPrice {
  padding-top: 1rem;
  color: #23aa49;
  font-size: 16px;
  font-style: normal;
  font-weight: 700;
  line-height: normal;
}
.productQty {
  padding-top: 1rem;
  padding-left: 0.5rem;

  color: #23aa49;
  font-size: 16px;
  font-style: normal;
  font-weight: 700;
  line-height: normal;
}
.addBtn {
  margin-top: 1rem;
  margin-left: 1rem;
  border-radius: 20%;
  background: #23aa49;
  color: white;
  display: flex;
  justify-content: center;
  align-items: center;
  font-size: 1rem;
  border: none;
  cursor: pointer;
}
.cartbtn {
  margin-top: 1.5rem;
  margin-left: 2.5rem;
  background: #23aa49;
  color: white;
  display: flex;
  justify-content: center;
  align-items: center;
  font-size: 1rem;
  border: none;
  cursor: pointer;
}
</style>
