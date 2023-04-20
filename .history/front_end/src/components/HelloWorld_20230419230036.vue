import axios from 'axios';

export default {
  data() {
    return {
      dataFromBackend: null
    };
  },
  created() {
    axios.get('/api/data').then(response => {
      this.dataFromBackend = response.data;
    });
  }
};
