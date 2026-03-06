import React from 'react';

interface OutputProps {
  output: string;
  error: string | null;
  isLoading: boolean;
}

export const Output: React.FC<OutputProps> = ({ 
  output, 
  error, 
  isLoading 
}) => {
  return (
    <div className="output-container">
      <div className="output-header">
        <h3>Output</h3>
      </div>

      <div className="output-panel">
        {isLoading && (
          <div className="loading-spinner">
            <div className="spinner"></div>
            <p>Processing...</p>
          </div>
        )}

        {error && !isLoading && (
          <div className="error-alert">
            <div className="error-icon">❌</div>
            <div className="error-content">
              <h4>Execution Error</h4>
              <p className="error-message">{error}</p>
            </div>
          </div>
        )}

        {!isLoading && !error && !output && (
          <div className="empty-state">
            <p>Your code output will appear here...</p>
          </div>
        )}

        {!isLoading && output && !error && (
          <pre className="output-text">{output}</pre>
        )}
      </div>

      <div className="output-footer">
        <small>Status: {isLoading ? 'Running' : error ? 'Error' : 'Completed'}</small>
      </div>
    </div>
  );
}

export default Output;