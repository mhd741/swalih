import React, { useState } from 'react';
import ReactDOM from 'react-dom';


const JournalApp = () => {
    const [entries, setEntries] = useState([]);
    const [input, setInput] = useState('');

    const addEntry = () => {
        if (input.trim()) {
            setEntries([...entries, input]);
            setInput('');
        } else {
            alert('Please write something before adding an entry.');
        }
    };

    const removeEntry = (index) => {
        setEntries(entries.filter((_, i) => i !== index));
    };

    return (
        <div style={{ margin: '20px', fontFamily: 'Arial, sans-serif' }}>
            <h1>Journal App</h1>
            <textarea
                value={input}
                onChange={(e) => setInput(e.target.value)}
                rows="4"
                cols="50"
                placeholder="Write your journal entry..."
            />
            <br />
            <button onClick={addEntry}>Add Entry</button>

            <div style={{ marginTop: '20px' }}>
                {entries.map((entry, index) => (
                    <div key={index} style={{ margin: '10px 0', padding: '10px', border: '1px solid #ccc', borderRadius: '5px' }}>
                        <p>{entry}</p>
                        <button
                            style={{ backgroundColor: 'red', color: 'white', border: 'none', padding: '5px 10px', cursor: 'pointer' }}
                            onClick={() => removeEntry(index)}
                        >
                            Remove
                        </button>
                    </div>
                ))}
            </div>
        </div>
    );
};

const App = () => {
    return (
        <div>
            <JournalApp />
        </div>
    );
};

ReactDOM.render(<App />, document.getElementById('root'));

