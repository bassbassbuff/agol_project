<script>
import axios from 'axios'


export default {
name: 'PrintSafetyDetails',

data() {
            return {
              pdfsrc:'',
              orderid:''
            }
},
mounted(){
  this.getChecklistDetails();
},
methods: {
  async getChecklistDetails() {

        let orderid = this.$route.params.id;
         
          let config = {
            headers: {
              "Content-Type": "application/x-www-form-urlencoded",
              // "Access-Control-Allow-Origin": "http://127.0.0.1:8000/",
            },
            responseType: 'blob'
          };

          await axios
          .get(`/checklist/${this.orderid},`,config)
          .then((response) => {
            const blob = new Blob([response.data], { type: "application/pdf" });
            const objectUrl = URL.createObjectURL(blob);
            this.pdfsrc = objectUrl;
            
          })
    }
}    
            
}

</script>

<template>   
    <pdf :src="pdfsrc"></pdf> 

</template>


