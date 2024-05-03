import React, { useState, useEffect } from 'react';
import axios from 'axios'
const apiStroke = "http://localhost:8000/api/"
const App = () => {
  const [data, setData] = useState(null);

  useEffect(() => {
    const fetchApiData = async () => {
      try {
        const response = await axios.get('http://localhost:8000/api/my-api/');
        setData(response.data);
      } catch (error) {
        console.error('Error fetching data:', error);
      }
    };

    fetchApiData();
  }, []);

  return (
    <div>
      <h1>Данные из API:</h1>
      {data ? (
        <div>
          <p>{data.message}</p>
        </div>
      ) : (
        <p>Загрузка данных...</p>
      )}
    </div>
  );
};

export default App;
export default App;
