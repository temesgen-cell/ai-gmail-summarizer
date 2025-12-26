import React, { useState, useEffect } from 'react';
import API from '../api/axiosConfig';
import '../styles/App.css';

const EmailList = () => {
    const [emails, setEmails] = useState([]);
    const [loading, setLoading] = useState(true);
    const [summarizingId, setSummarizingId] = useState(null);

    // 1. Fetch emails on component mount
    useEffect(() => {
        fetchEmails();
    }, []);

    const fetchEmails = async () => {
        try {
            const response = await API.get('/google/emails/');
            setEmails(response.data);
        } catch (error) {
            console.error("Error fetching emails:", error);
        } finally {
            setLoading(false);
        }
    };

    // 2. Handle AI Summary request
    const handleSummarize = async (id) => {
        setSummarizingId(id); // Set loading state for specific button
        try {
            const response = await API.post(`/google/summarize/${id}/`);
            
            // Update the local state so the summary appears immediately
            setEmails(prevEmails => 
                prevEmails.map(email => 
                    email.id === id ? { ...email, summary: response.data.summary } : email
                )
            );
        } catch (error) {
            alert("AI service is busy. Please try again later.");
        } finally {
            setSummarizingId(null);
        }
    };

    if (loading) return <div className="loader">Loading your inbox...</div>;

    return (
        <div className="email-container">
            <h1>AI-Powered Inbox</h1>
            <div className="email-list">
                {emails.length > 0 ? (
                    emails.map((email) => (
                        <div key={email.id} className="email-card">
                            <div className="email-header">
                                <span className="sender">{email.sender}</span>
                                <h3 className="subject">{email.subject}</h3>
                            </div>
                            
                            <p className="snippet">{email.snippet}</p>

                            {/* Show summary if it exists, otherwise show button */}
                            {email.summary ? (
                                <div className="summary-box">
                                    <strong>✨ AI Summary:</strong>
                                    <p>{email.summary}</p>
                                </div>
                            ) : (
                                <button 
                                    className="ai-btn"
                                    onClick={() => handleSummarize(email.id)}
                                    disabled={summarizingId === email.id}
                                >
                                    {summarizingId === email.id ? "Analyzing..." : "Get AI Summary"}
                                </button>
                            )}
                        </div>
                    ))
                ) : (
                    <p>No emails found. Please <a href="http://localhost:8000/google/login/">log in with Google</a>.</p>
                )}
            </div>
        </div>
    );
};

export default EmailList;