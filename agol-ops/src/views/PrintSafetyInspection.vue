<template>
    <div class="container">
        <div class="columns is-multiline">
            <div class="column is-12">
                <h1 class="title">Print Safety Inspection Lit</h1>
            </div>
                
            
            <div class="column is-12">
                <table class="table is-fullwidth">
                    <thead>
                        <tr>
                            <th>ID</th>
                            <th>Truck</th>
                            <th>Transporter</th>
                            <th>Trailer</th>                            
                            <th>Transporter</th>
                            
                            <th></th>
                        </tr>
                    </thead>

                    <tbody>
                        <tr
                            v-for="order in orders"
                            v-bind:key="order.id">                                
                                <td>{{ order.id }}</td>
                                <td>{{ order.truck_details['registration'] }}</td>
                                <td>{{ order.truck_details['transporter'] }}</td>
                                <td>{{ order.trailer_details['registration'] }}</td>
                                <td>{{ order.trailer_details['transporter'] }}</td>
                                
                                <td>
                                <!-- <button @click="submitForm" :value="order.id">PRINT -->
                                <button>
                                    <!-- {{orders}} -->
                                    
                                <router-link :to="`/print-safety/${order.id}`" class="button is-light">Print</router-link>
                                <!-- <router-link :to="{ name: 'Safetyform', params: { id: order.id }}" class="button is-light">Edit</router-link> -->
                                </button>
                                </td>
                               
                        </tr>

                    </tbody>
                </table>
            </div>
        </div>
    </div>
</template>

<script>
    import axios from 'axios'

    // import { toast } from 'bulma-toast'

    export default {
        name: 'SafetyInspection',
        data() {
            return {
                orders: [],
                // num_orders: ''
            }
        },
        mounted() {
            this.getOrders()
        },
        methods: {
            async getOrders() {
                // this.$store.commit('setIsLoading', true)
                // this.showNextButton = false
                // this.showPreviousButton = false
                await axios
                    .get(`/printsafety/`)
                    .then(response => {
                        console.log(response.data)
                        this.orders = response.data
                    })               
                
                    .catch(error => {
                        console.log(error)
                    })
                // this.$store.commit('setIsLoading', false)
            },
            async submitForm(value) {
        //         let config = {
        //     headers: {
        //         "Content-Type": 'application/octet-stream; charset=utf-8'
        //         "Content-Disposition": "attachment"; filename="filename.jpg"; filename*="filename.jpg"
              
        //     }           
        //   }

                await axios
                    .get(`/checklist/${value.target.value}`)
                    .then(response => {
                        const blob = new Blob([response.data], {type: response.data.type});
                        const url = window.URL.createObjectURL(blob);
                        const link = document.createElement('a');
                        link.href = url;
                        const contentDisposition = response.headers['content-disposition'];
                        let fileName = 'Safety Inspection';
                        if (contentDisposition) {
                            const fileNameMatch = contentDisposition.match(/filename="(.+)"/);
                            if (fileNameMatch.length === 2)
                                fileName = fileNameMatch[1];
                        }
                        link.setAttribute('download', fileName);
                        document.body.appendChild(link);
                        link.click();
                        link.remove();
                        window.URL.revokeObjectURL(url);
                                                })

            
                    .catch(error => {
                        console.log(error)
                    })
            }
            
        }
    }
</script>