import { NavLink } from 'react-router-dom'

function Apunte(props) {
    return (
        <div className="card">
        <div className="card-header">
          {props.titulo}
        </div>
        <div className="card-body">
          <p className="card-text">{props.contenido}</p>
          <NavLink to="/" className="btn btn-primary">Ver Apunte</NavLink>
        </div>
      </div>
    )
}

export default Apunte
