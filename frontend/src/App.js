import { useState, useEffect } from "react";
import axios from 'axios';

function App() {
  const [rentData, setRentData] = useState([]);
  const [error, setError] = useState(null);
  const [loading, setLoading] = useState(true);

  const url = 'http://localhost:8000/api/v1/rentdata/';

  useEffect(() => {
    axios
      .get(url)
      .then(response => {
        setRentData(response.data);
        setLoading(false);
      })
      .catch((error) => {
        setError(error.message);
        setLoading(false);
      });
  }, []);

  if (loading) {
    return (
      <div className="d-flex justify-content-center align-items-center vh-100">
        <div className="spinner-border" role="status">
          <span className="sr-only">Loading...</span>
        </div>
      </div>
    );
  }

  if (error) {
    return <p className="text-danger text-center mt-5">Error: {error}</p>;
  }

  return (
    <div className="container mt-4">
      <h1 className="text-center mb-4">Rent Data</h1>
      <table className="table table-bordered">
        <thead>
          <tr>
            <th scope="col">Apartment</th>
            <th scope="col">Income Bracket</th>
            <th scope="col">Rent Amount</th>
            <th scope="col">Lease Start Date</th>
            <th scope="col">Lease End Date</th>
            <th scope="col">Rent Paid Date</th>
          </tr>
        </thead>
        <tbody>
          {rentData.map((data) => (
            <tr key={data.id}>
              <td>{data.apartment.address}, {data.apartment.city}, {data.apartment.state}</td>
              <td>{data.income_bracket}</td>
              <td>${data.rent_amount}</td>
              <td>{data.lease_start_date}</td>
              <td>{data.lease_end_date ? data.lease_end_date : 'N/A'}</td>
              <td>{data.rent_paid_date}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default App;
