import logo from './logo.svg';
import './App.css';
import ReactDOM from 'react-dom';
import React from 'react';


/* This example requires Tailwind CSS v2.0+ */
import { PaperClipIcon } from '@heroicons/react/solid'

const axios = require('axios');
axios.defaults.headers = {
"Access-Control-Allow-Origin" : "*",
"Content-Type" : "application/json"
}

var myOrdonnance = {
  prescripteur: "Guillaume CUNY",
  medicaments: [],
  patient: {
    name: ""
  }
};

function MedicamentToTable(medicaments)
{
  return (
<div className="relative overflow-x-auto shadow-md sm:rounded-lg">
    <table className="w-full text-sm text-left text-gray-500 dark:text-gray-400">
        <thead className="text-xs text-gray-700 uppercase bg-gray-50 dark:bg-gray-700 dark:text-gray-400">
            <tr>
                <th scope="col" className="px-6 py-3">
                    Medicament
                </th>
                <th scope="col" className="px-6 py-3">
                    Dosage
                </th>
                <th scope="col" className="px-6 py-3">
                    Frequence
                </th>
                <th scope="col" className="px-6 py-3">
                    Durée
                </th>
                <th scope="col" className="px-6 py-3">
                    <span className="sr-only">Edit</span>
                </th>
            </tr>
        </thead>
        <tbody>
             {medicaments.map((medoc, index) => (
              <tr key={index} className="bg-white border-b dark:bg-gray-800 dark:border-gray-700">
                <th scope="row" className="px-6 py-4 font-medium text-gray-900 dark:text-white whitespace-nowrap">
                    {medoc.name}
                </th>
                <td className="px-6 py-4">
                    {medoc.dosage}
                </td>
                <td className="px-6 py-4">
                    {medoc.frequency}
                </td>
                <td className="px-6 py-4">
                    {medoc.duration}
                </td>
                <td className="px-6 py-4 text-right">
                    <a href="#" className="font-medium text-blue-600 dark:text-blue-500 hover:underline">Edit</a>
                </td>
            </tr>
             ))} 
        </tbody>
      </table>
    </div>
  )
}

function Example(props) {
  return (
    <form>
  <div className="mb-6">
    <label className="block mb-2 text-sm font-medium text-gray-900 dark:text-gray-300">Prescripteur</label>
    <input type="text" id="prescripteur" className="rounded-none rounded-r-lg bg-gray-50 border border-gray-300 text-gray-900 focus:ring-blue-500 focus:border-blue-500 block flex-1 min-w-0 w-full text-sm border-gray-300 p-2.5  dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" defaultValue={props.ordonnance.prescripteur} placeholder="Bonnie Green"/>
  </div>
  <div className="mb-6">
    <label className="block mb-2 text-sm font-medium text-gray-900 dark:text-gray-300">Patient</label>
    <input type="text" id="patient" className="rounded-none rounded-r-lg bg-gray-50 border border-gray-300 text-gray-900 focus:ring-blue-500 focus:border-blue-500 block flex-1 min-w-0 w-full text-sm border-gray-300 p-2.5  dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" defaultValue={props.ordonnance.patient.name} placeholder="Bonnie Green"/>
  </div>
  <div className="mb-6">
    <label className="block mb-2 text-sm font-medium text-gray-900 dark:text-gray-300">Prescription</label>
    {MedicamentToTable(props.ordonnance.medicaments)}
  </div>
  <div>
  <button onClick={RenderPDF} className="text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:ring-blue-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center mr-2 dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800">Valider</button>
  </div>
</form>
  )
}

async function StartRecording()
{
  ReactDOM.render(
    <App ordonnance = {myOrdonnance}
    startSpinning = {true}
    stopSpinning = {false}
    />, document.getElementById('root'));
  axios.get("http://localhost:5000/start")
  .then()
}

async function StopRecording()
{
  ReactDOM.render(
  <App ordonnance = {myOrdonnance}
  startSpinning = {false}
  stopSpinning = {true}
  />, document.getElementById('root'));
  axios.get("http://localhost:5000/end")
  .then(function(response){
    console.log(response);
    const ord = response.data;ReactDOM.render(
      <App ordonnance = {ord}
      startSpinning = {false}
      stopSpinning = {false}
      />, document.getElementById('root'));
      myOrdonnance = ord;
  }
  )
}

function returnSpinningRing()
{
  return (
    <svg role="status" className="inline mr-3 w-4 h-4 text-white animate-spin" viewBox="0 0 100 101" fill="none" xmlns="http://www.w3.org/2000/svg">
    <path d="M100 50.5908C100 78.2051 77.6142 100.591 50 100.591C22.3858 100.591 0 78.2051 0 50.5908C0 22.9766 22.3858 0.59082 50 0.59082C77.6142 0.59082 100 22.9766 100 50.5908ZM9.08144 50.5908C9.08144 73.1895 27.4013 91.5094 50 91.5094C72.5987 91.5094 90.9186 73.1895 90.9186 50.5908C90.9186 27.9921 72.5987 9.67226 50 9.67226C27.4013 9.67226 9.08144 27.9921 9.08144 50.5908Z" fill="#E5E7EB"/>
    <path d="M93.9676 39.0409C96.393 38.4038 97.8624 35.9116 97.0079 33.5539C95.2932 28.8227 92.871 24.3692 89.8167 20.348C85.8452 15.1192 80.8826 10.7238 75.2124 7.41289C69.5422 4.10194 63.2754 1.94025 56.7698 1.05124C51.7666 0.367541 46.6976 0.446843 41.7345 1.27873C39.2613 1.69328 37.813 4.19778 38.4501 6.62326C39.0873 9.04874 41.5694 10.4717 44.0505 10.1071C47.8511 9.54855 51.7191 9.52689 55.5402 10.0491C60.8642 10.7766 65.9928 12.5457 70.6331 15.2552C75.2735 17.9648 79.3347 21.5619 82.5849 25.841C84.9175 28.9121 86.7997 32.2913 88.1811 35.8758C89.083 38.2158 91.5421 39.6781 93.9676 39.0409Z" fill="currentColor"/>
    </svg>
  )
}

function App(props) {
  return (
    <div className='flex list-item'>
    <div className="App p-6 items-center justify-center">
        <h1 className="text-blue-400 font-extrabold">French ICA</h1>
        <p className="tracking-widest">L'IA au service de la relation médecin/patient</p>
    </div>
    <div className='flex row items-center justify-around'>
    <button onClick={StartRecording} className="text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:ring-blue-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center mr-2 dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800">
		{
      props.startSpinning ? (returnSpinningRing()) : (<></>)
    }
    Demarrer l'enregistrement
    </button>
    <button onClick={StopRecording} className="py-2.5 px-5 mr-2 text-sm font-medium text-gray-900 bg-white rounded-lg border border-gray-200 hover:bg-gray-100 hover:text-blue-700 focus:z-10 focus:ring-2 focus:ring-blue-700 focus:text-blue-700 dark:bg-gray-800 dark:text-gray-400 dark:border-gray-600 dark:hover:text-white dark:hover:bg-gray-700 inline-flex items-center">
		{
      props.stopSpinning ? (returnSpinningRing()) : (<></>)
    }
    Stopper l'enregistrement
    </button>
    </div>
    <Example
    ordonnance = {props.ordonnance}
    />
    </div>
  );
}

function RenderPDF()
{
  ReactDOM.render(
    <React.StrictMode>
      <GeneratePDF
      medicaments={myOrdonnance.medicaments}
      />
    </React.StrictMode>,
    document.getElementById('root')
  );
}

function GeneratePDF(props)
{
  return (
<html>
  <head>
    <meta charSet="utf-8"></meta>
    <title>Flexbox 0 — starting code</title>
    <link href="pdf.css" rel="stylesheet"></link>
  </head>
  <body>
    <header>
      <h1>Sample flexbox example</h1>
    </header>

    <section>
      <article>
        <h2>Docteur: Dr. Guillaume CUMY</h2>
        <h2>Patient: Mr. Fabrice VIOT:</h2>
        <h2>Prescriptions:</h2>
        {
          props.medicaments.map((medoc, index) => (
            <p> - {medoc.name} {medoc.dose} {medoc.frequency}</p>
          ))
        }
      </article>

      <article id="whiteP">
        <h2>Second article</h2>

        <p>Tacos actually microdosing, pour-over semiotics banjo chicharrones retro fanny pack portland everyday carry vinyl typewriter. Tacos PBR&B pork belly, everyday carry ennui pickled sriracha normcore hashtag polaroid single-origin coffee cold-pressed. PBR&B tattooed trust fund twee, leggings salvia iPhone photo booth health goth gastropub hammock.</p>
      </article>

      <article>
        <h2>Signature :</h2>
      </article>
    </section>
  </body>
</html>
  )
}

export default App;

