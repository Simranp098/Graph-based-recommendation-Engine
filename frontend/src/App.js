import React, { useState } from 'react';
import UserSelector from './components/UserSelector';
import Recommendations from './components/Recommendations';
import './App.css';

function App() {
const [selectedUserId, setSelectedUserId] = useState(null);

const handleUserSelect = (userId) => {
setSelectedUserId(userId);
};

return (
<div className="App">
<header className="App-header">
<h1>Graph-Based Recommendation Engine 🧠</h1>
<p>A demonstration of content personalization.</p>
</header>
<main>
<UserSelector onUserSelect={handleUserSelect} />
<Recommendations userId={selectedUserId} />
</main>
</div>
);
}

export default App;