import { useState, useEffect } from "react";

const useFetch = (url, request=null) => {

    const [data, setData] = useState(null);
    const [isLoading, setIsLoading] = useState(true);
    const [errors, setErrors] = useState(null);

    useEffect(() => {
        setTimeout(() => {
            fetch(url) 
            .then(response => {
                console.log(response);
                return response.json();
            })
            .then(data => {
                setData(data);
                setIsLoading(false);
            })
            .catch(err => {
                console.log(err);
                setErrors(err);
                setIsLoading(false);
            })
        }, 1000);
    }, [url]);

    return { data, isLoading, errors }
};

export default useFetch;