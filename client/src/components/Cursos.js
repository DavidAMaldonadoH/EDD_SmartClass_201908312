import { useState } from 'react';

import { Graphviz } from 'graphviz-react';

function Cursos(props) {
	const [dotSrc, setDotSrc] = useState('graph {  }');
	const [year, setYear] = useState('');
	const [semestre, setSemestre] = useState('');

	const getCursos = async () => {
		const res = await fetch(
			`http://localhost:3000/cursos/ver/${props.account.carnet}/${year}/${semestre}`
		);
		const data = await res.json();
		setDotSrc(data.dotSrc);
	};

	return (
		<div
			className="container d-flex align-items-start flex-column"
			style={{ marginTop: 0, paddingTop: 0 }}
		>
			<div className="keyContainer d-flex flex-row justify-content-center w-100">
				<label
					className="text-white text-center fw-bold bg-dark col-form-label"
					style={{ width: '20%', height: '50px' }}
				>
					Año
				</label>
				<textarea
					className="form-control"
					style={{ resize: 'none', width: '20%', height: '50px' }}
					onChange={(e) => setYear(e.target.value)}
				></textarea>
				<label
					className="text-white text-center fw-bold bg-dark col-form-label"
					style={{ width: '20%', height: '50px' }}
				>
					Semestre
				</label>
				<textarea
					className="form-control"
					style={{ resize: 'none', width: '20%', height: '50px' }}
					onChange={(e) => setSemestre(e.target.value)}
				></textarea>
				<button
					className="btn btn-info"
					style={{ width: '20%', height: '50px' }}
					onClick={getCursos}
				>
					Ver
				</button>
			</div>
			<div className="mt-2">
				<Graphviz
					className="graphviz"
					dot={dotSrc}
					options={{
						height: 350,
						width: 1250,
					}}
				/>
			</div>
		</div>
	);
}

export default Cursos;
