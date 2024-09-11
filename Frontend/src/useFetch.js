import { useState, useEffect } from "react";

const useFetch = (url) => {

    const [data, setData] = useState(null);
    const [isLoading, setIsLoading] = useState(true);
    const [errors, setErrors] = useState(null);

    useEffect(() => {
        setTimeout(() => {
            fetch(url) 
            .then(response => {
                if (!response.ok){
                    throw Error("could not fetch data")
                }
                return response.json();
            })
            .then(data => {
                setData(data);
                setIsLoading(false);
            })
            .catch(err => {
                setErrors(err.message);
                setIsLoading(false);
            })
        }, 1000);
    }, [url]);

    return { data, isLoading, errors }
};

export default useFetch;