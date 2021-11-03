import { NavLink } from "react-router-dom";

function NavBar1() {
	return (
		<nav className="navbar navbar-expand-sm navbar-dark bg-dark">
			<div className="container-fluid">
				<NavLink className="navbar-brand" to="/">
					Smart Class
				</NavLink>
				<button
					className="navbar-toggler"
					type="button"
					data-bs-toggle="collapse"
					data-bs-target="#navbarNav"
					aria-controls="navbarNav"
					aria-expanded="false"
					aria-label="Toggle navigation"
				>
					<span className="navbar-toggler-icon" />
				</button>
				<div className="collapse navbar-collapse" id="navbarNav">
					<ul className="navbar-nav ms-auto">
						<li className="nav-item">
							<NavLink className="nav-link" aria-current="page" to="/login">
								Login
							</NavLink>
						</li>
						<li className="nav-item">
							<NavLink className="nav-link" to="/register">
								Register
							</NavLink>
						</li>
					</ul>
				</div>
			</div>
		</nav>
	);
}

export default NavBar1;
