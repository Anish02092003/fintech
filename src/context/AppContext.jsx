import { createContext, useContext, useEffect, useState } from "react";

const AppContext = createContext();

export function AppProvider({ children }) {
  const [companyData, setCompanyData] = useState(() => {
    const saved = localStorage.getItem("companyData");
    return saved ? JSON.parse(saved) : null;
  });

  const [individualData, setIndividualData] = useState(() => {
    const saved = localStorage.getItem("individualData");
    return saved ? JSON.parse(saved) : null;
  });

  // -------------------------
  // Persist to localStorage
  // -------------------------
  useEffect(() => {
    if (companyData) {
      localStorage.setItem("companyData", JSON.stringify(companyData));
    }
  }, [companyData]);

  useEffect(() => {
    if (individualData) {
      localStorage.setItem("individualData", JSON.stringify(individualData));
    }
  }, [individualData]);

  return (
    <AppContext.Provider
      value={{
        companyData,
        setCompanyData,
        individualData,
        setIndividualData,
      }}
    >
      {children}
    </AppContext.Provider>
  );
}

export function useAppData() {
  return useContext(AppContext);
}