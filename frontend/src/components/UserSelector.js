import React from 'react';

// A mock list of users. In a real app, you might fetch this from an API.
const users = [
    { id: 1, name: 'Ronak' },
    { id: 2, name: 'Aisha' },
    { id: 3, name: 'Ben' },
];

function UserSelector({ onUserSelect }) {
    return (
        <div className="user-selector">
            <label htmlFor="user-select">Select a User:</label>
            <select
                id="user-select"
                onChange={(e) => onUserSelect(e.target.value)}
                defaultValue=""
            >
                <option value="" disabled>-- Choose a user --</option>
                {users.map(user => (
                    <option key={user.id} value={user.id}>
                        {user.name}
                    </option>
                ))}
            </select>
        </div>
    );
}

export default UserSelector;