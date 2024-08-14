import React, { useEffect, useState } from 'react';
import axios from 'axios';
import { API_BASE_URL } from '../config'; // Adjust the path if necessary

const Bookings = () => {
  const [bookings, setBookings] = useState([]);

  useEffect(() => {
    const fetchBookings = async () => {
      try {
        const response = await axios.get(`${API_BASE_URL}bookings/`);
        setBookings(response.data);
      } catch (error) {
        console.error('Error fetching bookings:', error);
      }
    };

    fetchBookings();
  }, []);

  return (
    <div>
      <h1>Bookings</h1>
      <ul>
        {bookings.map((booking) => (
          <li key={booking.id}>
            {booking.booking_date} - {booking.booking_time}
          </li>
        ))}
      </ul>
    </div>
  );
};

export default Bookings;
