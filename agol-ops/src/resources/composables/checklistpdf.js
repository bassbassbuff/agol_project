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
                        let response = await axios.get(`/checklist/${orderid.value}`,config)
                        const blob = new Blob([response.data], {type: response.data.type});
                        console.log(blob)
                        
                        const url = window.URL.createObjectURL(blob);
                        window.open(url, '_blank');
                        // const url = "/images/myw3schoolsimage"
                        
                        
                        // const contentDisposition = response.headers['content-disposition', 'application/octet-stream' ];
                        // let fileName = 'Safety Inspection';
                        // if (contentDisposition) {
                        //     const fileNameMatch = contentDisposition.match(/filename="(.+)"/);
                        //     if (fileNameMatch.length === 2)
                        //         fileName = fileNameMatch[1];
                        // } 
                        // let fileName = 'Safety Inspection'; 
                        const link = document.createElement('a');
                        link.href = url;                  
                        
                        link.setAttribute('download', fileName);
                        document.body.appendChild(link);
                        link.click();                        
                        link.remove();
                        window.URL.revokeObjectURL(url);        
        
       
    }




    return {
        getInspectionPrintout,
        
    }
}