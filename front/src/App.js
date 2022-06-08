import Home from "./pages/home/Home";
import Login from "./pages/login/Login";
import List from "./pages/list/List";
import ListOrder from "./pages/lisstOrder/ListOrder";
import ListCategory from "./pages/listCategory/ListCategory";
import Single from "./pages/single/Single";
import New from "./pages/new/New";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import { categoryInputs, userInputs ,orderInputs} from "./formSource";
import "./style/dark.scss";
import { useContext } from "react";
import { DarkModeContext } from "./context/darkModeContext";

function App() {
  const { darkMode } = useContext(DarkModeContext);

  return (
    <div className={darkMode ? "app dark" : "app"}>
      <BrowserRouter>
        <Routes>
          <Route path="/">
            <Route index element={<Home />} />
            <Route path="login" element={<Login />} />


            
            <Route path="users">
              <Route index element={<List />} />
              <Route path=":userId" element={<Single />} />
              <Route
                path="new"
                element={<New inputs={userInputs} title="Add New User" />}
              />
              
            </Route>

            <Route path="orders">
              <Route index element={<ListOrder />} />
              <Route path=":orderId" element={<Single />} />
              <Route
                path="new"
                element={<New inputs={orderInputs} title="Add New Order" />}
              />
              
            </Route>

            <Route path="category">
              <Route index element={<ListCategory />} />
              <Route path=":categoryId" element={<Single />} />
              <Route
                path="new"
                element={<New inputs={categoryInputs} title="Add New Category" />}
              />
              
            </Route>

            
          </Route>
        </Routes>
      </BrowserRouter>
    </div>
  );
}

export default App;
