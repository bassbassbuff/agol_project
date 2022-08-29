<template>
  <div class="container">
    <div class="columns is-multiline">
      
        <h1 class="title">BulkBalance</h1>

          <router-link :to="{ name: 'Home' }" class="button is-light mt-4"
            >Add Order</router-link
          >
        </div>

        <div>
          <table>
            <thead>
              <tr>
                <th>ID</th>
                <th>Created at</th>
                <th>Destination</th>
                <!-- <th>Driver</th>
                <th>Order Qty</th>
                <th>Status</th>
                <th>Trailer</th>
                <th>Truck</th> -->
                <th></th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="order in this.orders" :key="order.id">
                <td>{{ order.id }}</td>
                <td>{{ order.product }}</td>
                <td>{{ order.quantity }}</td>
                <!-- <td>{{ order.driver_details.name }}</td>
                <td>{{ order.order_quantity }}</td>
                <td>{{ order.status }}</td>
                <td>{{ order.trailer_details.registration }}</td>
                <td>{{ order.truck_details.registration }}</td> -->
              </tr>
            </tbody>
          </table>
        </div>
      </div>    
</template>

<script>
import axios from "axios";
export default {
  name: "BulkBalance",
  data() {
    return {
      orders: "",      
      query: "",
    };
  },
  mounted() {
    this.getOrders();
  },
  methods: {
    async getOrders() {
      // this.$store.commit('setIsLoading', true)
      this.showNextButton = false;
      this.showPreviousButton = false;

      let config = {
        headers: {
          Authorization: "Bearer " + localStorage.getItem("access_token"),
          "Content-Type": "application/json",
        },
      };

      await axios
        .get(`/bulk-order/`, config)
        .then((response) => {
          console.log(response.data);
          this.orders = response.data;
          console.log(Object.keys(this.orders));
          // this.num_orders = response.data.count;
        })
        .catch((error) => {
          console.log(error);
        });
      // this.$store.commit('setIsLoading', false)
    },
  },
};
</script>
