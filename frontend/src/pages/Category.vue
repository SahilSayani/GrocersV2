<script setup>
import ProductCard from "../components/ProductCard.vue";
</script>
<template>
  <div>
    {{ $route.params.id }}
    <div class="typography">{{ name }}</div>
    <div class="bg"></div>

    <div>
      {{ products }}
    </div>
    <div class="flex categories">
      <div v-for="product in products" :key="product.id">
        <ProductCard
          :id="product.id"
          :name="product.name"
          :price="product.price"
          :available-quantity="product.availableQuantity"
          :category-id="product.categoryId"
          :image="product.image"
        />
      </div>
    </div>
  </div>
</template>

<script>
import { API_URL } from "../constants";
export default {
  data() {
    return {
      name: "",
      products: [],
    };
  },
  methods: {
    getCategory() {
      fetch(API_URL + "/category/" + this.$route.params.id)
        .then(async (response) => await response.text())
        .then((data) => {
          this.name = data;
        });
    },
    getProducts() {
      fetch(API_URL + "/category/" + this.$route.params.id + "/products")
        .then(async (response) => await response.json())
        .then((data) => {
          this.products = data;
        });
    },
  },
  mounted() {
    this.getCategory();
    this.getProducts();
  },
};
</script>
.categories {
  margin: 2%;
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 5rem;
  flex-wrap: wrap;
}
<style scoped></style>
