
package fp.tipos;

import java.time.Duration;
import java.util.ArrayList;
import java.util.List;
import java.util.Objects;

import fp.utiles.Checkers;

public class Viaje {
	private Double precio;
	private int distancia;
	private Duration duracion;
	private TipoViaje tipoViaje;
	private List<Parada> trayecto; // Ordenadas de origen a destino.
	
	public void restriccion1() {
		Checkers.check("El trayecto debe tener al menos "
				+ "dos paradas (origen y destino).", 
				getTrayecto().size() >= 2);
	}
	
	public void restriccion2() {
		Checkers.check("La distancia, la duración "
				+ "y el precio deben ser mayores que cero.",
				getDistancia() > 0 
				&& getDuracion().getSeconds() > 0
				&& getPrecio() > 0);
	}
	
	public void restriccion3() {
		if(getTrayecto().size() == 2) {
			getTipoViaje();
			Checkers.check("El tipo de viaje de un "
					+ "viaje con solo un origen "
					+ "y un destino no puede ser "
					+ "TRANSBORDO.", tipoViaje != TipoViaje
					.TRANSBORDO);
		}
	}

	public Viaje(Double precio, int distancia, 
			Duration duracion, TipoViaje tipoViaje, 
			Parada origen, Parada destino) {
		super();
		this.precio = precio;
		this.distancia = distancia;
		this.duracion = duracion;
		this.tipoViaje = tipoViaje;
		this.trayecto = new ArrayList<Parada>(trayecto);
		trayecto.add(origen);
		trayecto.add(destino);
		
		restriccion1();
		restriccion2();
		restriccion3();
	} 
	
	public Viaje(Double precio, int distancia, Duration duracion, TipoViaje tipoViaje, List<Parada> trayecto) {
		super();
		this.precio = precio;
		this.distancia = distancia;
		this.duracion = duracion;
		this.tipoViaje = tipoViaje;
		this.trayecto = new ArrayList<Parada>(trayecto);
		
		restriccion1();
		restriccion2();
		restriccion3();
	}

	public Double getPrecio() {
		return precio;
	}

	public void setPrecio(Double precio) {
		this.precio = precio;
	}

	public int getDistancia() {
		return distancia;
	}

	public void setDistancia(int distancia) {
		this.distancia = distancia;
	}

	public Duration getDuracion() {
		return duracion;
	}

	public void setDuracion(Duration duracion) {
		Checkers.check("Duración incorrecta",
				duracion.compareTo(Duration.ZERO) > 0);
		this.duracion = duracion;
	}

	public TipoViaje getTipoViaje() {
		return tipoViaje;
	}

	public void setTipoViaje(TipoViaje tipoViaje) {
		this.tipoViaje = tipoViaje;
	}
	
	public List<Parada> getTrayecto() {
		return trayecto;
	}

	public void setTrayecto(List<Parada> trayecto) {
		this.trayecto = trayecto;
	}

	public Double getVelocidadMedia()  {
		return distancia / (duracion.getSeconds() / 3600.0);
	}
	
	public Integer getNumeroParadas() {
		return getTrayecto().size() - 2 - getNumeroTransbordos();
	}
	
	public String getOrigen() {
		return getTrayecto().get(0).nombre();
	}
	
	public String getDestino() {
		return getTrayecto().get(getTrayecto().size() - 1).nombre();
	}
	
	public List<String> getParadas() {
		List<Parada> inter = getTrayecto().subList(1, 
				getNumeroParadas() + 1);
		List<String> res = new ArrayList<>();
		for (Parada p : inter) {
			res.add(p.nombre());
		}
		return res;	
	}
	
	public Integer getNumeroTransbordos() {
		Integer numTransbordos = 0;
		if(getTipoViaje().equals(TipoViaje.TRANSBORDO)) {
			numTransbordos = 
					calcularRepetidosConsecutivos(getTrayecto());
		}
		return numTransbordos;
	}
	
	private Integer calcularRepetidosConsecutivos(List<Parada> trayecto) {
		Integer cont = 0;
		for (int i=0; i<trayecto.size() - 2; i++) {
			if (trayecto.get(i).nombre().equals(
					trayecto.get(i + 1).nombre())) {
				cont ++;
			}
		}
		return cont;
	}

	@Override
	public int hashCode() {
		return Objects.hash(trayecto);
	}

	@Override
	public boolean equals(Object obj) {
		if (this == obj)
			return true;
		if (obj == null)
			return false;
		if (getClass() != obj.getClass())
			return false;
		Viaje other = (Viaje) obj;
		return Objects.equals(trayecto, other.trayecto);
	}

	@Override
	public String toString() {
		return "Viaje [precio=" + precio + ", distancia=" + distancia + ", duracion=" + duracion + ", tipoViaje="
				+ tipoViaje + ", trayecto=" + trayecto + "]";
	}
}