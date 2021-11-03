import userIcon from '../icons/user-solid.svg';

function UserInfo(props) {
    return (
        <div className="card mb-3 w-100 p-3 border-primary">
        <div className="row g-0">
            <div className="col-md-2 d-flex justify-content-center align-items-center">
                <img
                    src={userIcon}
                    className="img-fluid rounded-start"
                    alt="..."
                    style={{ height: '100px', width: '100px' }}
                />
            </div>
            <div className="col-md-8">
                <div className="card-body">
                    <h5 className="card-title">Usuario: {props.account.nombre}</h5>
                    <p className="card-text">Carnet: {props.account.carnet}<br />Correo: {props.account.correo}</p>
                </div>
            </div>
        </div>
    </div>
    )
}

export default UserInfo
