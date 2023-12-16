<template>
  <h1 class="typography">Cart🧺</h1>
  <table>
    <thead class="flex cartTable"></thead>
    <tbody>
      <tr v-for="(product, index) in cartProducts" :key="index">
        <div class="cartCard">
          <div class="cartCardName">
            <td>{{ product.name }}</td>
          </div>
          <div class="cartCardPrice">
            <td>{{ product.price }}</td>
          </div>
          <div class="cartCardCounter">
            <td>
              <button
                class="cartbutton"
                @click="decrementQuantity(index)"
                :disabled="product.quantity === 1"
              >
                -
              </button>
              {{ product.quantity }}
              <button class="cartbutton" @click="incrementQuantity(index)">
                +
              </button>
            </td>
          </div>
          <div class="cartCardPrice">
            <td>{{ product.price * product.quantity }}</td>
          </div>
        </div>
      </tr>
    </tbody>
  </table>
  <p class="typography total">Total: {{ cartTotal }}</p>
</template>

<script>
import { API_URL } from '../constants';

export default {
  data() {
    return {
      cartProducts: [
        { name: "Login to view Cart", price: 0, quantity: 0 },
      ],
    };
  },
  computed: {
    cartTotal() {
      return this.cartProducts.reduce(
        (total, product) => total + product.price * product.quantity,
        0
      );
    },
  },
  methods: {
    incrementQuantity(index) {
      this.cartProducts[index].quantity++;
    },
    decrementQuantity(index) {
      this.cartProducts[index].quantity--;
    },
    async fetchCart() {
      try {
        const res = await fetch(API_URL + "/cart", {
          headers: {
            Authorization: "Bearer " + localStorage.getItem("token"),
          },
        });

        const items = await res.json();

        this.cartProducts = items;
      } catch (e) {
        console.error(e);
      }
    },
  },
  mounted() {
    this.fetchCart();
  },
};
</script>
<style>
h1 {
  border-bottom: 1px solid #617986;
  padding-bottom: 1rem;
}
table {
  display: flex;
  align-items: center;
  justify-content: center;
}
.cartTable {
  display: flex;
  justify-content: space-around;
  align-items: center;
  padding: 0 10px;
}
.cartCard {
  width: 40rem;
  height: 6rem;
  flex-shrink: 0;
  border-radius: 16px;
  background: #1a3848;
  overflow: hidden;
  display: flex;
  margin: 1rem;
}
.cartCardName {
  padding: 2rem;
  font-size: 1.5rem;
  font-style: normal;
  font-weight: 500;
  line-height: normal;
}
.cartCardPrice {
  padding: 2rem;
  color: #59c778;
  font-size: 1.5rem;
  font-style: normal;
  font-weight: 500;
  line-height: normal;
}
.cartCardCounter {
  padding: 2rem;
  color: #59c778;
  font-size: 1.5rem;
  font-style: normal;
  font-weight: 500;
  line-height: normal;
}
.cartbutton {
  height: 2rem;
  width: 2rem;
  border-radius: 50%;
  background: #0d1f29;
  border: #203744;
  cursor: pointer;
  font-weight: 900;
  font-size: 0.8rem;
}
button:hover {
  background: #59c778;
  color: #0d1f29;
}
.total {
  display: flex;
  justify-content: flex;
  margin-right: 10%;
  font-size: 1.5rem;
  font-style: normal;
  font-weight: 500;
  line-height: normal;
}
</style>
