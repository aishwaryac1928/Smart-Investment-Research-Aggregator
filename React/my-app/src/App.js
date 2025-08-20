
// import React, { useState } from "react";
// import "./App.css";

// function App() {
//   const [company, setCompany] = useState("");
//   const [ticker, setTicker] = useState("");
//   const [brief, setBrief] = useState(null);
//   const [loading, setLoading] = useState(false);
//   const [error, setError] = useState("");

//   const handleSubmit = async (e) => {
//     e.preventDefault();
//     setLoading(true);
//     setError("");
//     setBrief(null);

//     try {
//       const response = await fetch("/api/research", {
//         method: "POST",
//         headers: { "Content-Type": "application/json" },
//         body: JSON.stringify({ company, ticker }),
//       });

//       if (!response.ok) {
//         const err = await response.json();
//         throw new Error(err.detail || "Something went wrong");
//       }

//       const data = await response.json();
//       setBrief(data.brief);
//     } catch (err) {
//       setError(err.message);
//     } finally {
//       setLoading(false);
//     }
//   };

//   return (
//     <div className="App">
//       <h1>Smart Investment Research Aggregator</h1>
//       <form onSubmit={handleSubmit}>
//         <input
//           type="text"
//           placeholder="Company Name"
//           value={company}
//           onChange={(e) => setCompany(e.target.value)}
//           required
//         />
//         <input
//           type="text"
//           placeholder="Ticker"
//           value={ticker}
//           onChange={(e) => setTicker(e.target.value)}
//           required
//         />
//         <button type="submit">Get Research Brief</button>
//       </form>

//       {loading && <p>Loading...</p>}
//       {error && <p style={{ color: "red" }}>{error}</p>}

//       {brief && (
//         <div className="brief-result">
//           <h2>Consensus View</h2>
//           <p>{brief.consensus_view}</p>

//           <h2>Conflicting Opinions</h2>
//           <ul>
//             {brief.conflicting_opinions.map((item, idx) => (
//               <li key={idx}>{item}</li>
//             ))}
//           </ul>

//           <h2>Confidence Score</h2>
//           <p>{brief.confidence_score}</p>

//           <h2>Key Risks</h2>
//           <ul>
//             {brief.key_risks.map((risk, idx) => (
//               <li key={idx}>{risk}</li>
//             ))}
//           </ul>
//         </div>
//       )}
//     </div>
//   );
// }

// export default App;

import React, { useState } from "react";
import { saveAs } from "file-saver";
import { Document, Packer, Paragraph, TextRun } from "docx";
import "./App.css";

function App() {
  const [company, setCompany] = useState("");
  const [ticker, setTicker] = useState("");
  const [brief, setBrief] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    setError("");
    setBrief(null);

    try {
      const response = await fetch("/api/research", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ company, ticker }),
      });

      if (!response.ok) {
        const err = await response.json();
        throw new Error(err.detail || "Something went wrong");
      }

      const data = await response.json();
      setBrief(data.brief);
    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  };

  // ✅ Export to DOCX
  const handleExport = () => {
    if (!brief) return;

    const doc = new Document({
      sections: [
        {
          children: [
            new Paragraph({ text: "Research Brief", heading: "Heading1" }),
            new Paragraph({ text: `Company: ${company} (${ticker})`, spacing: { after: 300 } }),

            new Paragraph({ text: "Consensus View", heading: "Heading2" }),
            new Paragraph(brief.consensus_view),

            new Paragraph({ text: "Conflicting Opinions", heading: "Heading2" }),
            ...brief.conflicting_opinions.map(
              (item) => new Paragraph({ text: `• ${item}` })
            ),

            new Paragraph({ text: "Confidence Score", heading: "Heading2" }),
            new Paragraph(String(brief.confidence_score)),

            new Paragraph({ text: "Key Risks", heading: "Heading2" }),
            ...brief.key_risks.map(
              (risk) => new Paragraph({ text: `• ${risk}` })
            ),
          ],
        },
      ],
    });

    Packer.toBlob(doc).then((blob) => {
      saveAs(blob, `${company}_${ticker}_ResearchBrief.docx`);
    });
  };

  return (
    <div className="App">
      <h1>Smart Investment Research Aggregator</h1>
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          placeholder="Company Name"
          value={company}
          onChange={(e) => setCompany(e.target.value)}
          required
        />
        <input
          type="text"
          placeholder="Ticker"
          value={ticker}
          onChange={(e) => setTicker(e.target.value)}
          required
        />
        <button type="submit">Get Research Brief</button>
      </form>

      {loading && <p className="loading">Loading...</p>}
      {error && <p style={{ color: "red" }}>{error}</p>}

      {brief && (
        <div className="brief-result">
          <h2>Consensus View</h2>
          <p>{brief.consensus_view}</p>

          <h2>Conflicting Opinions</h2>
          <ul>
            {brief.conflicting_opinions.map((item, idx) => (
              <li key={idx}>{item}</li>
            ))}
          </ul>

          <h2>Confidence Score</h2>
          <p>{brief.confidence_score}</p>

          <h2>Key Risks</h2>
          <ul>
            {brief.key_risks.map((risk, idx) => (
              <li key={idx}>{risk}</li>
            ))}
          </ul>

          {/* ✅ Export button */}
          <button className="export-btn" onClick={handleExport}>
            Export as DOCX
          </button>
        </div>
      )}
    </div>
  );
}

export default App;
