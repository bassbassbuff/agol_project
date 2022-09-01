import { ref } from 'vue'
import axios from "axios";
import { useRoute } from 'vue-router';

export default function useSafetyInspectionForm() {
    const truck = ref('')
    const trailer = ref('')
    const questions = ref([])
    const route = useRoute()

    const orderid = ref(route.params.id)

    let config = {
        headers: {
          "Content-Type": "application/x-www-form-urlencoded",
          // "Access-Control-Allow-Origin": "http://127.0.0.1:8000/",
        },
        responseType: 'blob'
      };


    const getInspectionPrintout = async () => {
        await axios.get(`/checklist/${orderid.value}`,config)
        console.log(response.data)
        truckid.value = response.data.truck_details.id
        
        
        ;
    }




    return {
        getInspectionPrintout,
        
    }
}