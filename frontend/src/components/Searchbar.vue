<template>
    <div class="flex searchfield">
        <svg class="searchicon" xmlns="http://www.w3.org/2000/svg"  height="1em" viewBox="0 0 512 512"><!--! Font Awesome Free 6.4.2 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license (Commercial License) Copyright 2023 Fonticons, Inc. --><path d="M416 208c0 45.9-14.9 88.3-40 122.7L502.6 457.4c12.5 12.5 12.5 32.8 0 45.3s-32.8 12.5-45.3 0L330.7 376c-34.4 25.2-76.8 40-122.7 40C93.1 416 0 322.9 0 208S93.1 0 208 0S416 93.1 416 208zM208 352a144 144 0 1 0 0-288 144 144 0 1 0 0 288z"/></svg>

            <input class="typography2 searchbar"
                type="text"
                v-model="searchQuery"
                @input="performSearch"
                placeholder="Search ..." 
            />
    </div>
</template>

<script>
export default {
    data() {
        return {
            searchQuery: '',
            searchResults: []
        }
    },
    methods: {
        performSearch() {
         this.$emit('search', this.searchQuery);
        },
        
    }
}
</script>
<style>
.searchfield{
    margin-left: 38% !important;
    display: flex;
    width: 25rem;
    padding-bottom: 0.5rem;
    flex-direction: row;
    justify-content: space-around;
    align-items: center;
    gap: 0.5rem;
    border-radius: 2rem;
    margin-left: 2rem;
    background-color: #1A3848;
    padding: 0.5rem;
}
.searchbar{
    font-size: 1rem;
    font-weight: 400;
    color: #ffffff;
    margin-top: 0.5rem;
    background: transparent;
    
    margin: 15px 0; 
    padding: 6px 4px;
    width: 65%;
    outline: none;
    border: 1px solid #bbb;
    border-radius: 20px;
    display: inline-block;
    -webkit-box-sizing: border-box;
    -moz-box-sizing: border-box;
    box-sizing: border-box;
    -webkit-transition: 0.2s ease all;
    -moz-transition: 0.2s ease all;
    -ms-transition: 0.2s ease all;
    -o-transition: 0.2s ease all;
    transition: 0.2s ease all;
}
.searchicon{
    margin-bottom: 10px;
    fill:#23aa49;
    height: 2rem;
    
}
</style>