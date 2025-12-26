// frontend/src/api/axiosConfig.js
import axios from 'axios';

const API = axios.create({
    baseURL: 'http://localhost:8000', // Change this to your production URL later
    timeout: 10000, // 10 seconds timeout for AI processing
    headers: {
        'Content-Type': 'application/json',
    }
});

// If you use Django's default CSRF protection, this helps handle it:
API.defaults.xsrfCookieName = 'csrftoken';
API.defaults.xsrfHeaderName = 'X-CSRFToken';

export default API;