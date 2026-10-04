import ReactDOM from 'react-dom/client';
import {ClassComponent, FuncComponent} from './component.js';
import './index.css';

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <ClassComponent firstName = "Joey" />
)

const funcroot = ReactDOM.createRoot(document.getElementById('funcroot'));
funcroot.render(FuncComponent("Broden", "Smithy"));
