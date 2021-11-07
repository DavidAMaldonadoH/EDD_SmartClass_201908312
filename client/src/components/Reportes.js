import { useState } from 'react';

import { Graphviz } from 'graphviz-react';

function Reportes() {
	const [dotSrc, setDotSrc] = useState('graph { }');

    const reporteApuntes = async () => {
		const res = await fetch('http://localhost:3000/reporteapuntes');
		const data = await res.json();
		setDotSrc(data.dotSrc);
	};

    const reporteAVL1 = async () => {
		const res = await fetch('http://localhost:3000/reporteavl1');
		const data = await res.json();
		setDotSrc(data.dotSrc);
	};

	const reporteAVL2 = async () => {
		const res = await fetch('http://localhost:3000/reporteavl2');
		const data = await res.json();
		setDotSrc(data.dotSrc);
	};

	const reporteGrafo = async () => {
		const res = await fetch('http://localhost:3000/redcurriculum');
		const data = await res.json();
		setDotSrc(data.dotSrc);
	};

	return (
		<div
			className="modal fade"
			id="ReportesModal"
			tabIndex={-1}
			aria-labelledby="ReportesModalLabel"
			aria-hidden="true"
		>
			<div className="modal-dialog modal-dialog-scrollable modal-xl">
				<div className="modal-content">
					<div className="modal-header">
						<h5 className="modal-title" id="ReportesModalLabel">
							Reportes
						</h5>
						<button
							type="button"
							className="btn-close"
							data-bs-dismiss="modal"
							aria-label="Close"
						></button>
					</div>
					<div className="modal-body">
						<div className="btn-group" role="group" aria-label="Basic example">
							<button type="button" className="btn btn-primary" onClick={reporteApuntes}>
								Apuntes
							</button>
							<button type="button" className="btn btn-primary" onClick={reporteAVL1}>
								Estudiantes
							</button>
							<button type="button" className="btn btn-primary" onClick={reporteAVL2}>
								Estudiantes Encriptados
							</button>
							<button type="button" className="btn btn-primary" onClick={reporteGrafo}>
								Grafo
							</button>
						</div>
						<Graphviz
							className="graphviz"
							dot={dotSrc}
							options={{
								height: 500,
								width: 2500,
							}}
						/>
					</div>
					<div className="modal-footer">
						<button type="button" className="btn btn-primary" data-bs-dismiss="modal">
							Close
						</button>
					</div>
				</div>
			</div>
		</div>
	);
}

export default Reportes;
