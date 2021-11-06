import { useState } from 'react';

import ApunteForm from './ApunteForm';
import ApuntesList from './ApuntesList';

function ApuntesPage(props) {
	const [notes, setNotes] = useState([]);

	const fetchAputes = async () => {
		const res = await fetch(`http://localhost:3000/apuntes_usuario/${props.account.carnet}`);
		const data = await res.json();
		setNotes(data.apuntes)
		return data;
	};

	return (
		<div className="container" style={{ marginTop: 0, paddingTop: 0 }}>
			<div className="w-100">
				<nav>
					<div className="nav nav-tabs" id="nav-tab" role="tablist">
						<button
							className="nav-link active"
							id="apuntesTab"
							data-bs-toggle="tab"
							data-bs-target="#apuntes"
							type="button"
							role="tab"
							aria-controls="apuntes"
							aria-selected="true"
							onClick={fetchAputes}
						>
							Apuntes
						</button>
						<button
							className="nav-link"
							id="nuevoApuntetab"
							data-bs-toggle="tab"
							data-bs-target="#nuevoApunte"
							type="button"
							role="tab"
							aria-controls="nuevoApunte"
							aria-selected="false"
						>
							Nuevo Apunte
						</button>
					</div>
				</nav>
				<div className="tab-content" id="nav-tabContent">
					<div className="tab-pane fade" id="apuntes" role="tabpanel" aria-labelledby="apuntesTab">
						<ApuntesList notes={notes}/>
					</div>
					<div
						className="tab-pane fade"
						id="nuevoApunte"
						role="tabpanel"
						aria-labelledby="nuevoApuntetab"
					>
						<ApunteForm account={props.account} />
					</div>
				</div>
			</div>
		</div>
	);
}

export default ApuntesPage;
