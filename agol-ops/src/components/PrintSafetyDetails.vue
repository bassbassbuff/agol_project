<script>
import axios from 'axios'
import useSafetyForm from "../resources/composables/trucks";
import {onMounted} from "vue";

export default {
name: 'PrintSafetyDetails',
setup() {
  const { truck, trailer, truckid, trailerid, orderid, getTruck } = useSafetyForm()
  
  onMounted(getTruck())

  return {
    truckid,
    trailerid,
    orderid,
    truck,
    trailer,
  

    
  }
},
data() {
            return {
              checklistDetails:[]
            }
},
mounted(){
  this.getChecklistDetails();
},
methods: {
  async getChecklistDetails() {
         
          let config = {
            headers: {
              "Content-Type": "application/json",
              "Access-Control-Allow-Origin": "http://localhost:8000/",
            },
          };

          await axios
          .get(`/checklist/${this.orderid}`)
          .then((response) => {
            this.checklistDetails = response.data
            console.log(response.data)
          })
    }
}    
            
}

</script>

<template>
    <div>
    <h4>Truck Reg: {{ truck }} </h4>
    <h4>Trailer Reg: {{ trailer }} </h4>
    </div>
    <!-- <div v-for="(choice, question, index) in checklistDetails"> -->
    <div  v-for="ques in checklistDetails"
                            v-bind:key="ques.id"
                       >
    <div>   
      <p>{{ques.question['question_desc']}} {{ques.checklist_choice}}</p>
    </div>  
      
    </div>
   

</template>


