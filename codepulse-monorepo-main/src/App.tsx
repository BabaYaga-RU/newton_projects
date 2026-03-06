import { useState } from 'react';
import MonacoEditor from '@monaco-editor/react';
import logo from './assets/logo.png';
import './App.css';

interface ImportMetaEnv {
  VITE_API_URL?: string;
}

const API_URL = ((import.meta as unknown) as { env: ImportMetaEnv }).env.VITE_API_URL || 'https://codepulse-monorepo-backend.vercel.app';

export function App() {
  const [code, setCode] = useState('// Welcome to CodePulse\nconsole.log("Hello World");');
  const [output, setOutput] = useState('');
  const [error, setError] = useState<string | null>(null);
  const [isLoading, setIsLoading] = useState(false);

  const handleExecute = async () => {
    setIsLoading(true);
    setOutput('');
    setError(null);

    try {
      const response = await fetch(`${API_URL}/api/execute`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ code }),
      });

      const data = await response.json();

      if (data.output || data.error) {
        setOutput(data.output || '');
        setError(data.error || null);
      } else {
        setError('Unexpected server response format.');
      }
    } catch (err) {
      setError(err instanceof Error ? err.message : 'Execution error occurred');
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div className="app">
      <header>
        <h1>
          <img src={logo} alt="CodePulse Logo" className="header-logo" />
          CodePulse - Simple IDE
        </h1>
        <p>Online code execution environment</p>
      </header>

      <div className="container">
        <div className="editor-section">
          <label>Source Code:</label>
          <MonacoEditor
            height="450px"
            defaultLanguage="javascript"
            value={code}
            onChange={(value) => setCode(value || '')}
            theme="vs-dark"
            options={{
              minimap: { enabled: false },
              fontSize: 14,
              automaticLayout: true,
              scrollBeyondLastLine: false,
            }}
          />
          <button
            onClick={handleExecute}
            disabled={isLoading}
            className="execute-btn"
          >
            {isLoading ? "Processing..." : "Execute"}
          </button>
        </div>

        <div className="output-section">
          <label>Output:</label>
          <div className="output-box">
            {isLoading && <p className="loading">Executing...</p>}
            {error && <p className="error">Error: {error}</p>}
            {output && !error && (
              <pre className="output-text">
                <code>{output}</code>
              </pre>
            )}
            {!isLoading && !error && !output && (
              <p className="placeholder">Click "Execute" to run your code.</p>
            )}
          </div>
        </div>
      </div>

      <footer className="footer">
        <p>CodePulse - Simple Online IDE</p>
      </footer>
    </div>
  );
}

export default App;