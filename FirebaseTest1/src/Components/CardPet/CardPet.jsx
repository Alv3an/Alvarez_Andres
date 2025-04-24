import * as React from 'react';
import Card from '@mui/material/Card';
import CardActions from '@mui/material/CardActions';
import CardContent from '@mui/material/CardContent';
import CardMedia from '@mui/material/CardMedia';
import Button from '@mui/material/Button';
import Typography from '@mui/material/Typography';

const CardPet = ({ pets }) => {
    return (
        <Card sx={{ maxWidth: 345 }}>
            <CardMedia
                component="img"
                alt="pito.jpg"
                height="200"
                image={pets.img}
            />
            <CardContent>
                <Typography gutterBottom variant="h5" component="div">
                    {pets.nombre}
                </Typography>
                <Typography gutterBottom variant="h5" component="div">
                    {pets.edad}
                </Typography>
                <Typography gutterBottom variant="h5" component="div">
                    {pets.especie}
                </Typography>
            </CardContent>
            <CardActions>
                <Button size="small">Share</Button>
                <Button size="small">Learn More</Button>
            </CardActions>
        </Card>
    );
}

export default CardPet